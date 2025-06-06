# NSAccessibilityElementLoading

**Framework**: AppKit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to support loading.

**Availability**:
- macOS 10.13+

## Declaration

```swift
protocol NSAccessibilityElementLoading : NSObjectProtocol
```

#### Overview

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol declares.

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

 Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityElement(withToken: NSAccessibilityLoadingToken) -> (any NSAccessibilityElementProtocol)?](nsaccessibilityelementloading/accessibilityelement(withtoken:).md)
  Loads the target accessibility element with the specified load token.
- [func accessibilityRangeInTargetElement(withToken: NSAccessibilityLoadingToken) -> NSRange](nsaccessibilityelementloading/accessibilityrangeintargetelement(withtoken:).md)
  Returns the range that specifies the area of interest in text-based accessibility elements with the specified load token.
- [typealias NSAccessibilityLoadingToken](nsaccessibilityloadingtoken.md)
  A token type for loading accessibility elements.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSAccessibilityProgressIndicator](nsaccessibilityprogressindicator.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a progress indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelementloading)*