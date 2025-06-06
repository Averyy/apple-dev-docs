# value(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns an array containing the results of invoking [`value(forKey:)`](nsarray/value(forkey:).md) using `key` on each of the array’s objects.

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
func value(forKey key: String) -> Any
```

#### Return Value

The value of the retrieved key.

#### Discussion

The returned array contains `NSNull` elements for each object that returns `nil`.

## Parameters

- `key`: The key to retrieve.

## See Also

- [func setValue(Any?, forKey: String)](nsarray/setvalue(_:forkey:).md)
  Invokes [`setValue(_:forKey:)`](nsarray/setvalue(_:forkey:).md) on each of the array’s items using the specified `value` and `key`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/value(forkey:))*