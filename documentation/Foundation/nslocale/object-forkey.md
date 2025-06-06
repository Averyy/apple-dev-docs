# object(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns the value of the component corresponding to the specified key.

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
func object(forKey key: NSLocale.Key) -> Any?
```

#### Return Value

The object corresponding to `key`.

## Parameters

- `key`: The component for which to return the corresponding value. For possible values, see  .

## See Also

- [func displayName(forKey: NSLocale.Key, value: Any) -> String?](nslocale/displayname(forkey:value:).md)
  Returns the display name for the given locale component value.
- [NSLocale.Key](nslocale/key.md)
  The keys used to access components of a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/object(forkey:))*