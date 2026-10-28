# init(targetElement:targetRange:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a rotor item result from the specified target element and text range.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(targetElement: any NSObjectProtocol, targetRange: UITextRange?)
```

```objc
- (instancetype) initWithTargetElement:(id<NSObject>) targetElement targetRange:(UITextRange *) targetRange;
```

## Return Value

An initialized rotor item result.

## Parameters

- `targetElement`: The target element of the rotor.
- `targetRange`: The text range for an element that contains text, such as a text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotoritemresult/init(targetelement:targetrange:))*