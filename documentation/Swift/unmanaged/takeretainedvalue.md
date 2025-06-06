# takeRetainedValue()

**Framework**: Swift  
**Kind**: method

Gets the value of this unmanaged reference as a managed reference and consumes an unbalanced retain of it.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func takeRetainedValue() -> Instance
```

#### Return Value

The object referenced by this `Unmanaged` instance.

#### Discussion

This is useful when a function returns an unmanaged reference and you know that you’re responsible for releasing the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unmanaged/takeretainedvalue())*