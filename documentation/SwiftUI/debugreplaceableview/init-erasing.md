# init(erasing:)

**Framework**: SwiftUI  
**Kind**: init

Creates a debug replaceable view erasing the given view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)
- Unknown ?+ - Deprecated

## Declaration

```swift
init<V>(erasing view: V) where V : View
```

#### Discussion

You don’t use this initializer directly. Instead SwiftUI creates this type on your behalf when building in debug mode.

This type acts similarly to an `AnyView` in that it type-erases its content, however it depends on the underlying type of the value not actually changing as it is in place of an opaque result type. As such, it .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/debugreplaceableview/init(erasing:))*