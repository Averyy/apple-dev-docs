# responds(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the receiving class responds to a given selector.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func responds(to aSelector: Selector) -> Bool
```

```objc
+ (BOOL) respondsToSelector:(SEL) aSelector;
```

## Return Value

[`true`](../../Swift/true.md) if the receiving class responds to `aSelector` messages, otherwise [`false`](../../Swift/false.md).

## Parameters

- `aSelector`: A selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsproxy/responds(to:))*