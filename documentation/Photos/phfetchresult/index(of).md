# index(of:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Returns the lowest index whose corresponding object in the fetch result is equal to the specified object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func index(of anObject: ObjectType) -> Int
```

```objc
- (NSUInteger) indexOfObject:(ObjectType) anObject;
```

## Return Value

The lowest index whose corresponding object in the fetch result is equal to `anObject`, or `NSNotFound` if no such object is in the fetch result.

## Discussion

Starting at index `0`, this method sends an `==` message to each object in the fetch result until it finds a match or reaches the end of the fetch result. This method passes the `anObject` parameter to each `==` message.

## Parameters

- `anObject`: An object.

## See Also

### Finding Objects in a Fetch Result
- [func index(of: ObjectType, in: NSRange) -> Int](./index%28of,in%29.md)
  Returns the lowest index within the specified range whose corresponding object in the fetch result is equal to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresult/index(of:))*