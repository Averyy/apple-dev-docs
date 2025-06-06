# openInPlace

**Framework**: UIKit  
**Kind**: property

A key containing a flag that indicates whether a document must be copied before you use it.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let openInPlace: UIApplication.OpenURLOptionsKey
```

#### Discussion

When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), you must copy the document to maintain access to it. If the flag is not set, you also must copy the document before you can use it.

If the document does not need to be copied, you can open it in place in your implementation of the [`application(_:open:options:)`](uiapplicationdelegate/application(_:open:options:).md) method. For information about declaring whether your app wants the ability to open iCloud Drive documents in place, see the description of the [`LSSupportsOpeningDocumentsInPlace`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW13) information property list key. For an example of an app that opens iCloud Drive documents in place, see [`ShapeEdit: Building a Simple iCloud Document App`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/ShapeEdit/Introduction/Intro.html#//apple_ref/doc/uid/TP40016100).

## See Also

- [static let sourceApplication: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/sourceapplication.md)
  A key containing the bundle ID of the app that sent the open-URL request to your app.
- [static let annotation: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/annotation.md)
  A key containing the information passed to a document interaction controller object’s annotation property.
- [static let eventAttribution: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/eventattribution.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/openurloptionskey/openinplace)*