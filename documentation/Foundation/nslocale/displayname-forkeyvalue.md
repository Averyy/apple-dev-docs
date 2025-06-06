# displayName(forKey:value:)

**Framework**: Foundation  
**Kind**: method

Returns the display name for the given locale component value.

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
func displayName(forKey key: NSLocale.Key, value: Any) -> String?
```

#### Return Value

The display name for `value`.

#### Discussion

Not all locale property keys have values with display name values.

You can use the [`identifier`](nslocale/key/identifier.md) key to get the name of a locale in the language of another locale, as illustrated in the following examples.

The following example uses the `en_GB` locale.

## Parameters

- `key`: The locale property key of  . For possible values, see  .
- `value`: A value for  .

## See Also

- [func object(forKey: NSLocale.Key) -> Any?](nslocale/object(forkey:).md)
  Returns the value of the component corresponding to the specified key.
- [NSLocale.Key](nslocale/key.md)
  The keys used to access components of a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/displayname(forkey:value:))*