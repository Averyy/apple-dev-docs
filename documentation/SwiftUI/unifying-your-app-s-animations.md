# Unifying your app’s animations

**Framework**: SwiftUI

Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.

#### Overview

Many apps use a combination of SwiftUI, UIKit, and AppKit to build and animate their interfaces. In iOS 18 and later, you can use SwiftUI animations in UIKit and AppKit. SwiftUI provides a wide range of standard as well as custom animation types.

![A conceptual illustration of a disclosure indicator, shown animating frame by frame from its collapsed position to its expanded position.](/images/com.apple.SwiftUI/Unifying-your-app-s-animations@2x.png)

SwiftUI, UIKit, and AppKit use different underlying implementations for animation. Apps that use multiple frameworks for animation might encounter certain issues, such as syncing animation timing or other inconsistencies, that can be difficult to troubleshoot and lead to a suboptimal user experience. Use SwiftUI animations to animate UI across all of these frameworks to create a more consistent and seamless experience on every platform.

##### Create a Swiftui Animation

To create a SwiftUI animation in UIKit or AppKit, import SwiftUI and create a SwiftUI [`Animation`](animation.md). Then, pass that animation as a parameter into the [`animate(_:changes:completion:)`](https://developer.apple.com/documentation/uikit/uiview/animate(_:changes:completion:)) class method on `UIView`, or the [`animate(_:changes:completion:)`](https://developer.apple.com/documentation/appkit/nsanimationcontext/animate(_:changes:completion:)) class method on `NSAnimationContext`. The following examples compare how you can create a basic spring animation using a SwiftUI [`Animation`](animation.md) type across SwiftUI, UIKit, and AppKit.

**SwiftUI**:

```swift
struct ContentView: View {
    @State private var position = CGPoint(x: 200, y: 200)
    @State private var frame = CGSize(width: 100, height: 100)
    
    var body: some View {
        Rectangle()
            .fill(Color.blue)
            .frame(width: frame.width, height: frame.height)
            .position(position)
        Button("Animate") {
            // Use a spring animation to animate the view to a new location.
            let animation = Animation.spring(duration: 0.8)
            withAnimation(animation) {
                position = CGPoint(x: 100, y: 100)
            }
        }
    }
}
```

**UIKit**:

```swift
import SwiftUI

let position = CGPoint(x: 200, y: 200)
let frame = CGSize(width: 100, height: 100)
let buttonPosition = CGPoint(x: 200, y: 400)
let buttonFrame = CGSize(width: 100, height: 100)

override func viewDidLoad() {
    super.viewDidLoad()
            
    let myView = UIView(frame: CGRect(origin: position, size: frame))
    myView.backgroundColor = .systemBlue
    
    let myButton = UIButton(primaryAction: UIAction(title: "Animate") { _ in
        // Use a spring animation to animate the view to a new location.
        let animation = SwiftUI.Animation.spring(duration: 0.8)
        UIView.animate(animation) {
            myView.center = CGPoint(x: 100, y: 100)
        }
    })
    myButton.frame = CGRect(origin: buttonPosition, size: buttonFrame)
    
    view.addSubview(myView)
    view.addSubview(myButton)
}
```

**AppKit**:

```swift
import SwiftUI

let myView = NSView(frame: CGRect(origin: CGPoint(x: 50, y: 50), 
                                  size: CGSize(width: 50, height: 50)))

override func viewDidLoad() {
    super.viewDidLoad()
    
    let myButton = NSButton(title: "Animate", target: self, action: #selector(animateView))
    view.addSubview(myButton)

    myView.wantsLayer = true
    myView.layer?.backgroundColor = NSColor.blue.cgColor
    view.addSubview(myView)
}

@objc
func animateView() {
    // Use a spring animation to change the size of the view.
    let animation = SwiftUI.Animation.spring(duration: 0.8)
    NSAnimationContext.animate(animation) {
        myView.frame.size = CGSize(width: 100, height: 100)
    }
}
```

##### Use Completion Handlers with Swiftui Animations

You can provide an optional completion handler to these animation methods, which the system calls automatically after the animations complete. The following examples show a completion handler that changes the background color of the view to indicate when the animation completes.

**SwiftUI**:

```swift
struct ContentView: View {
    @State private var color = Color.blue
    @State private var position = CGPoint(x: 200, y: 200)
    @State private var frame = CGSize(width: 100, height: 100)
    
    var body: some View {
        Rectangle()
            .fill(color)
            .frame(width: frame.width, height: frame.height)
            .position(position)
        Button("Animate") {
            // Use a smooth spring animation to animate the view to a new location.
            withAnimation(.smooth) {
                position = CGPoint(x: 100, y: 100)
            } completion: {
                // When the animation completes, change the color of the view.
                color = Color.red
            }
        }
    }
}
```

**UIKit**:

```swift
import SwiftUI

let position = CGPoint(x: 200, y: 200)
let frame = CGSize(width: 100, height: 100)
let buttonPosition = CGPoint(x: 200, y: 400)
let buttonFrame = CGSize(width: 100, height: 100)

override func viewDidLoad() {
    super.viewDidLoad()
        
    let myView = UIView(frame: CGRect(origin: position, size: frame))
    myView.backgroundColor = .systemBlue

    let myButton = UIButton(primaryAction: UIAction(title: "Animate") { _ in
        // Use a smooth spring animation to animate the view to a new location.
        UIView.animate(.smooth) {
            myView.center = CGPoint(x: 100, y: 100)
        } completion: {
            // When the animation completes, change the color of the view.
            myView.backgroundColor = .systemRed
        }
    })
    myButton.frame = CGRect(origin: buttonPosition, size: buttonFrame)

    view.addSubview(myView)
    view.addSubview(myButton)
}
```

**AppKit**:

```swift
import SwiftUI

let myView = NSView(frame: CGRect(origin: CGPoint(x: 50, y: 50), 
                                  size: CGSize(width: 50, height: 50)))

override func viewDidLoad() {
    super.viewDidLoad()
    
    let myButton = NSButton(title: "Animate", target: self, action: #selector(animateView))
    view.addSubview(myButton)

    myView.wantsLayer = true
    myView.layer?.backgroundColor = NSColor.blue.cgColor
    view.addSubview(myView)
}

@objc
func animateView() {
    // Use a smooth spring animation to change the size of the view.
    NSAnimationContext.animate(.smooth) {
        self.myView.frame.size = CGSize(width: 100, height: 100)
    } completion: {
        // When the animation completes, change the color of the view.
        self.myView.layer?.backgroundColor = NSColor.red.cgColor
    }
}
```

##### Retarget a Swiftui Animation

Similar to animations in SwiftUI views, you can smoothly retarget the animations you perform using the [`animate(_:changes:completion:)`](https://developer.apple.com/documentation/uikit/uiview/animate(_:changes:completion:)) class method on `UIView` or the [`animate(_:changes:completion:)`](https://developer.apple.com/documentation/appkit/nsanimationcontext/animate(_:changes:completion:)) class method on `NSAnimationContext`. Retargeting a SwiftUI animation uses the velocity from the previous animations to carry the animation forward with continuous velocity, creating a fluid animation experience. The following examples show retargeting an in-progress animation.

**SwiftUI**:

```swift
struct ContentView: View {
    @State private var position = CGPoint(x: 200, y: 200)
    @State private var frame = CGSize(width: 100, height: 100)
    
    var body: some View {
        Rectangle()
            .fill(Color.blue)
            .frame(width: frame.width, height: frame.height)
            .position(position)
        Button("Animate") {
            Task {
                // Begin an animation to move the view to a new location.
                withAnimation(.spring(duration: 1.0)) {
                    position = .zero
                }
                
                try await Task.sleep(for: .seconds(0.5))

                // Retarget the running animation to move the view to a different location.
                withAnimation(.spring) {
                    position = CGPoint(x: 100, y: 400)
                }
            }
        }
    }
}
```

**UIKit**:

```swift
import SwiftUI

let position = CGPoint(x: 200, y: 200)
let frame = CGSize(width: 100, height: 100)
let buttonPosition = CGPoint(x: 200, y: 400)
let buttonFrame = CGSize(width: 100, height: 100)

override func viewDidLoad() {
    super.viewDidLoad()
    
    let myView = UIView(frame: CGRect(origin: position, size: frame))
    myView.backgroundColor = .systemBlue
    
    let myButton = UIButton(primaryAction: UIAction(title: "Animate") { _ in
        Task { 
            // Begin an animation to move the view to a new location.
            UIView.animate(.spring(duration: 1.0)) {
                myView.center = CGPoint(x: 200, y: 200)
            }
            
            try await Task.sleep(for: .seconds(0.5))
            
            // Retarget the running animation to move the view to a different location.
            UIView.animate(.spring) {
                myView.center = CGPoint(x: 100, y: 400)
            }
        }
    })
    myButton.frame = CGRect(origin: buttonPosition, size: buttonFrame)
    
    view.addSubview(myView)
    view.addSubview(myButton)
}
```

**AppKit**:

```swift
import SwiftUI

let myView = NSView(frame: CGRect(origin: CGPoint(x: 50, y: 50), 
                                  size: CGSize(width: 50, height: 50)))

override func viewDidLoad() {
    super.viewDidLoad()
    
    let myButton = NSButton(title: "Animate", target: self, action: #selector(animateView))
    view.addSubview(myButton)

    myView.wantsLayer = true
    myView.layer?.backgroundColor = NSColor.blue.cgColor
    view.addSubview(myView)
}

@objc
func animateView() {
    Task {
        // Begin an animation to change the size of the view.
        NSAnimationContext.animate(.spring(duration: 1)) {
            myView.frame.size = CGSize(width: 100, height: 100)
        }

        try await Task.sleep(for: .seconds(0.5))

        // Retarget the running animation to change the view to a different size.
        NSAnimationContext.animate(.spring) {
            myView.frame.size = CGSize(width: 75, height: 75)
        }
    }
}
```

##### Troubleshoot Animations

Syncing animations across frameworks can surface differing behavior across implementations. Keep these tips in mind when you troubleshoot animations in your app:

- SwiftUI animations run on a background thread in your app’s process.
- SwiftUI animations don’t have a backing [`CAAnimation`](https://developer.apple.com/documentation/quartzcore/caanimation), which differentiates them from [`UIView`](https://developer.apple.com/documentation/uikit/uiview) animations.
- SwiftUI animations aren’t compatible with [`UIViewPropertyAnimator`](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator) or `UIView` keyframe animations.

For more information about providing a great animation experience in your app, see [`Enhance your UI animations and transitions`](https://developer.apple.comhttps://developer.apple.com/wwdc24/10145/).

## See Also

- [struct Animation](animation.md)
  The way a view changes over time to create a smooth visual transition from one state to another.
- [func withAnimation<Result>(Animation?, () throws -> Result) rethrows -> Result](withanimation(_:_:).md)
  Returns the result of recomputing the view’s body with the provided animation.
- [static func animate(Animation, changes: () -> Void, completion: (() -> Void)?)](../uikit/uiview/animate(_:changes:completion:).md)
- [static func animate(Animation, changes: () -> Void, completion: (() -> Void)?)](../appkit/nsanimationcontext/animate(_:changes:completion:).md)
  Animate changes to one or more views using the specified SwiftUI animation.
- [class NSHostingController](nshostingcontroller.md)
  An AppKit view controller that hosts SwiftUI view hierarchy.
- [class NSHostingView](nshostingview.md)
  An AppKit view that hosts a SwiftUI view hierarchy.
- [class NSHostingMenu](nshostingmenu.md)
  An AppKit menu with menu items that are defined by a SwiftUI View.
- [struct NSHostingSizingOptions](nshostingsizingoptions.md)
  Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [class NSHostingSceneRepresentation](nshostingscenerepresentation.md)
  An AppKit type that hosts and can present SwiftUI scenes
- [struct NSHostingSceneBridgingOptions](nshostingscenebridgingoptions.md)
  Options for how hosting views and controllers manage aspects of the associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/unifying-your-app-s-animations)*