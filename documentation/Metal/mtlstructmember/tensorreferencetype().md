# tensorReferenceType()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Provides a description of the underlying tensor type when this struct member holds a tensor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func tensorReferenceType() -> MTLTensorReferenceType?
```

```objc
- (MTLTensorReferenceType *) tensorReferenceType;
```

## Return Value

A description of the tensor type that this struct member holds, or `nil` if this struct member doesn’t hold a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructmember/tensorreferencetype())*