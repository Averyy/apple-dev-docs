# containsValue(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether an encoded value is available for a string.

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
func containsValue(forKey key: String) -> Bool
```

```objc
- (BOOL) containsValueForKey:(NSString *) key;
```

## Discussion

Subclasses must override this method if they perform keyed coding.

The string is passed as `key`.

## See Also

### Inspecting a Coder
- [var allowsKeyedCoding: Bool](./allowskeyedcoding.md)
  A Boolean value that indicates whether the receiver supports keyed coding of objects.
- [var decodingFailurePolicy: NSCoder.DecodingFailurePolicy](./decodingfailurepolicy-swift.property.md)
  The action the coder should take when decoding fails.
- [NSCoder.DecodingFailurePolicy](./decodingfailurepolicy-swift.enum.md)
  Policies describing the action the coder should take when encountering decode failures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/containsvalue(forkey:))*