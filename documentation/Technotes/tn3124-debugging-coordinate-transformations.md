# TN3124: Debugging coordinate space issues

**Framework**: Technotes

Learn techniques to help debug any coordinate space issue.

#### Overview

Working with coordinate spaces is an essential part of developing any graphics-based app. Issues related to assumptions or misinterpretations of a coordinate space are difficult to debug, or even identify. Read this technote to discover effective strategies for diagnosing and debugging coordinate space issues.

#### Recognize the Issue

Coordinate space issues can be difficult to recognize, but there are some common symptoms that can help to diagnose them:

- Unexpected or absent visual appearance
- Incorrect behavior of user-interaction
- Wrong values after a coordinate conversion

Assume that there is a coordinate space issue that needs to be debugged if you notice any of these symptoms in your app.

#### Identify the Coordinate Spaces Involved

Coordinate spaces are ubiquitous in the graphics world. Even simple apps will involve many different coordinate spaces. Identifying the coordinate spaces involved is essential to debugging issues with them.

Consider the following SwiftUI snippet:

```swift
struct ContentView: View {
    
    @State private var uiImage = UIImage()
    
    var body: some View {
        VStack {
            Image(uiImage: uiImage)
            Button("Hello") {
                print("World.")
            }
        }
    }
}
```

This snippet, while simple, actually involves five different coordinate spaces:

1. The local coordinate space of the `VStack`.
2. The local coordinate space of the `Image`.
3. The local coordinate space of the `Button`.
4. The local coordinate space of the `UIImage`.
5. The global coordinate space of `SwiftUI`.

#### Create a Focused Sample

Coordinate space issues are often very complex and difficult to reason about. Creating a focused sample project that visualizes origins, logs transforms and bounding boxes, and utilizes known points is an extremely effective tool for debugging coordinate space issues.

#### Visualize the Origin

The best first step towards understanding a coordinate space is to visualize its origin.

> ⚠️ **Warning**: Do not rely on textual descriptions of a coordinate space, they are easy to misinterpret.

Do not rely on textual descriptions of a coordinate space, they are easy to misinterpret.

Projects targeting visionOS can use [`Diagnosing issues in the appearance of a running app`](https://developer.apple.com/documentation/Xcode/diagnosing-issues-in-the-appearance-of-your-running-app). In other contexts, the exact code to visualize the origin will differ depending on the framework involved.

Some frameworks offer built-in ways to visualize certain origins. For example, `ARView` and `ARSCNView` both have API to visualize the world origin for debugging:

```swift
view.debugOptions.insert(.showWorldOrigin)
```

`ARView` has additional API to visualize anchor origins:

```swift
view.debugOptions.insert(.showAnchorOrigins)
```

Other frameworks may not have origin visualization API to aid in debugging, but it is always possible to write visualization code for any coordinate space. For example, this snippet visualizes the origin of any SwiftUI `View`:

```swift
import SwiftUI

extension View {
    /// Visualizes the origin of any View for debugging purposes.
    /// The x-axis is red, the y-axis is green.
    public func showOrigin() -> some View {
        modifier(CoordinateAxes())
    }
}

private struct CoordinateAxes: ViewModifier {
        
    func body(content: Content) -> some View {
        content.overlay {
            
            GeometryReader { geometry in
                
                let size = geometry.size
                
                let smallestDim = min(size.width, size.height)
                
                // Set length to be at least 20 points.
                let length = max(smallestDim * 0.2, 20)
                let thickness = length / 7
                
                // X-axis.
                Color.red
                    .frame(width: length, height: thickness)
                    .position(.init(x: length / 2, y: thickness / 2))
                
                // Y-axis.
                Color.green
                    .frame(width: thickness, height: length)
                    .position(.init(x: thickness / 2, y: length / 2))
            }
        }
    }
}
```

Visualizing an origin could be all that is necessary to realize where the error is.

#### Understand Input Expectations

Sometimes an API requires inputs that are already in a particular coordinate space. Otherwise its output is invalid.

Consider the `UIView` method, [`hitTest(_:with:)`](https://developer.apple.com/documentation/UIKit/UIView/hitTest(_:with:)). This method accepts a `CGPoint` as input, and uses it to perform a hit-test on the view. The problem here is that its results aren’t valid for  `CGPoint`, you must provide a `CGPoint` in the view’s local coordinate space to get a valid result.

When you have results that don’t make sense, it is a good idea to evaluate the APIs you are using to produce the results, and verify that you have provided inputs to them in the coordinate spaces they are expecting.

#### Use Known Points

Using known points is an effective graphics debugging technique.

Consider an app that runs a `VNDetectRectanglesRequest` on a `CMSampleBuffer` stream, displays the stream in an `AVCaptureVideoPreviewLayer`, and then attempts to draw the detected rectangles on top of the preview layer in an overlay `CALayer`, but the drawing doesn’t appear as expected. After gaining an understanding of each coordinate space involved in the drawing process (the `AVCaptureVideoPreviewLayer`, the overlay `CALayer`, and the `VNRectangleObservation`) by visualizing their origins, it can be helpful to draw a known point, instead of trying to debug this on the fly with a dynamic video stream. In this specific example, you might use `CGRect(x: 0, y: 0, width: 0.25, height: 0.25)` as the input, a rectangle that you would expect to cover one quarter of the preview image when drawn correctly.

Being consistent with the data you feed through a coordinate conversion pipeline allows you to clearly see the effects of any changes you make when debugging.

#### Log Transforms and Bounding Boxes

Logging the transform and bounding box of a visual element is a simple but effective debugging technique.

Consider a scenario where your app is inserting a 3D model into a scene, but you don’t see the 3D model where you expected to see it. By logging the transform and bounding box of the model, you discover that the scale and the bounding box of the model is very large. This is a very good indication that the model is so large that the current viewpoint of the 3D scene is  of the model. You remedy the situation by setting the model’s scale factor to a smaller value.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3124-debugging-coordinate-transformations)*