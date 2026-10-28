# object(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (id) objectForKey:(NSLocaleKey) key;
```

## Return Value

The object corresponding to `key`.

## Parameters

- `key`: The component for which to return the corresponding value. For possible values, see [`NSLocale.Key`](./key.md).

## See Also

### Accessing Locale Information by Key
- [func displayName(forKey: NSLocale.Key, value: Any) -> String?](./displayname%28forkey,value%29.md)
  Returns the display name for the given locale component value.
- [NSLocale.Key](./key.md)
  The keys used to access components of a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/object(forkey:))*