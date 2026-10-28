# getMultiArrayForStateNamed:handler:

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Gets a mutable view into a state buffer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```objc
- (void) getMultiArrayForStateNamed:(NSString *) stateName handler:(void (^)(MLMultiArray *buffer)) handler;
```

## Discussion

The underlying state buffer’s address can differ for each call; one shall not access the state buffer outside of the closure.

## Parameters

- `handler`: Block to access the state buffer through `MLMultiArray`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlstate/getmultiarrayforstatenamed:handler:)*