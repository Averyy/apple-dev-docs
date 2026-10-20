# isEqual(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that indicates whether the receiver and a given object are equal.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func isEqual(_ object: Any?) -> Bool
```

```objc
- (BOOL) isEqual:(id) object;
```

#### Return Value

[`YES`](../yes.md) if the receiver and `anObject` are equal, otherwise [`NO`](../no.md).

#### Discussion

This method defines what it means for instances to be equal. For example, a container object might define two containers as equal if their corresponding objects all respond [`YES`](../yes.md) to an [`isEqual(_:)`](./isequal%28_%29.md) request. See the [`NSData`](../../Foundation/nsdata.md), [`NSDictionary`](../../Foundation/nsdictionary.md), [`NSArray`](../../Foundation/nsarray.md), and [`NSString`](../../Foundation/nsstring.md) class specifications for examples of the use of this method.

If two objects are equal, they must have the same hash value. This last point is particularly important if you define [`isEqual(_:)`](./isequal%28_%29.md) in a subclass and intend to put instances of that subclass into a collection. Make sure you also define [`hash`](./hash.md) in your subclass.

## Parameters

- `object`: The object to be compared to the receiver. May be `nil`, in which case this method returns [`NO`](../no.md).

## See Also

### Identifying and Comparing Objects
- [var hash: Int](./hash.md)
  Returns an integer that can be used as a table address in a hash table structure.
- [func `self`() -> Self](./self%28%29.md)
  Returns the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/isequal(_:))*