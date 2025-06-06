# isEqual(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether the receiver and a given object are equal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func isEqual(_ object: Any?) -> Bool
```

#### Return Value

[`YES`](yes.md) if the receiver and `anObject` are equal, otherwise [`NO`](no.md).

#### Discussion

This method defines what it means for instances to be equal. For example, a container object might define two containers as equal if their corresponding objects all respond [`YES`](yes.md) to an [`isEqual(_:)`](nsobjectprotocol/isequal(_:).md) request. See the [`NSData`](https://developer.apple.com/documentation/Foundation/NSData), [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), and [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) class specifications for examples of the use of this method.

If two objects are equal, they must have the same hash value. This last point is particularly important if you define [`isEqual(_:)`](nsobjectprotocol/isequal(_:).md) in a subclass and intend to put instances of that subclass into a collection. Make sure you also define [`hash`](nsobjectprotocol/hash.md) in your subclass.

## Parameters

- `object`: The object to be compared to the receiver. May be  , in which case this method returns  .

## See Also

- [var hash: Int](nsobjectprotocol/hash.md)
  Returns an integer that can be used as a table address in a hash table structure.
- [func `self`() -> Self](nsobjectprotocol/self.md)
  Returns the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/isequal(_:))*