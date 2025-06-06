# sender

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The object on behalf of which to perform the menu element’s primary action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sender: Any? { get }
```

#### Discussion

The system populates this property during the execution of the menu element’s action (its handler or selector).

## See Also

- [func performWithSender(Any?, target: Any?)](uimenuleaf/performwithsender(_:target:).md)
  Performs the element’s primary action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuleaf/sender)*