# init(sessionDelegate:)

**Framework**: UIKit  
**Kind**: init

Initializes a find interaction object with the delegate object you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(sessionDelegate: any UIFindInteractionDelegate)
```

#### Return Value

Returns a find interaction object with the associated delegate.

#### Discussion

Create an object that conforms to the [`UIFindInteractionDelegate`](uifindinteractiondelegate.md) protocol and assign it to this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/init(sessiondelegate:))*