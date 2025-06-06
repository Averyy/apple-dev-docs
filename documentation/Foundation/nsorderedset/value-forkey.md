# value(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns an ordered set containing the results of invoking `valueForKey:` using key on each of the ordered set’s objects.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func value(forKey key: String) -> Any
```

#### Return Value

The ordered set of the values for the retrieved key. The returned ordered set might not have the same number of members as the receiver.

#### Discussion

The returned ordered set will not contain any elements corresponding to instances of `valueForKey:` returning `nil`, nor will it contain duplicates.

## Parameters

- `key`: The key to retrieve.

## See Also

- [func setValue(Any?, forKey: String)](nsorderedset/setvalue(_:forkey:).md)
  Invokes `setValue:forKey:` on each of the receiver’s members using the specified value and key


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/value(forkey:))*