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

**Swift**:

```swift
let frLocale = NSLocale(localeIdentifier: "fr_FR")
print(frLocale.displayNameForKey(NSLocaleIdentifier, value: "fr_FR")!)
// "français (France)"
print(frLocale.displayNameForKey(NSLocaleIdentifier, value: "en_US")!)
// "anglais (États-Unis)"
```

**Objective-C**:

```objc
NSLocale *frLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"fr_FR"];
NSLog(@"%@", [frLocale displayNameForKey:NSLocaleIdentifier value:@"fr_FR"]);
// "français (France)"
NSLog(@"%@", [frLocale displayNameForKey:NSLocaleIdentifier value:@"en_US"]);
// "anglais (États-Unis)"
```

The following example uses the `en_GB` locale.

**Swift**:

```swift
let gbLocale = NSLocale(localeIdentifier: "en_GB")
print(gbLocale.displayNameForKey(NSLocaleIdentifier, value: "fr_FR")!)
// "French (France)"
print(gbLocale.displayNameForKey(NSLocaleIdentifier, value: "en_US")!)
// "English (United States)"
```

**Objective-C**:

```objc
NSLocale *gbLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_GB"];
NSLog(@"%@", [gbLocale displayNameForKey:NSLocaleIdentifier value:@"fr_FR"]);
// "French (France)"
NSLog(@"%@", [gbLocale displayNameForKey:NSLocaleIdentifier value:@"en_US"]);
// "English (United States)"
```

## Parameters

- `key`: The locale property key of `value`. For possible values, see [`NSLocale.Key`](nslocale/key.md).
- `value`: A value for `key`.

## See Also

- [func object(forKey: NSLocale.Key) -> Any?](nslocale/object(forkey:).md)
  Returns the value of the component corresponding to the specified key.
- [NSLocale.Key](nslocale/key.md)
  The keys used to access components of a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/displayname(forkey:value:))*