# setPersistentDomain(_:forName:)

**Framework**: Foundation  
**Kind**: method

Sets a dictionary for the specified persistent domain.

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
func setPersistentDomain(_ domain: [String : Any], forName domainName: String)
```

#### Discussion

Calling this method is equivalent to initializing a user defaults object with [`init(suiteName:)`](userdefaults/init(suitename:).md) passing `domainName`, and calling the [`set(_:forKey:)`](userdefaults/set(_:forkey:)-8ab6d.md) method for each key-value pair in `domain`.

When a persistent domain is changed, an [`didChangeNotification`](userdefaults/didchangenotification.md) is posted.

## Parameters

- `domain`: A dictionary of keys and values you want to assign to the domain.
- `domainName`: The name of the domain whose contents you want to set.

## See Also

- [func persistentDomain(forName: String) -> [String : Any]?](userdefaults/persistentdomain(forname:).md)
  Returns a dictionary representation of the defaults for the specified domain.
- [func removePersistentDomain(forName: String)](userdefaults/removepersistentdomain(forname:).md)
  Removes the contents of the specified persistent domain from the user’s defaults.
- [func persistentDomainNames() -> [Any]](userdefaults/persistentdomainnames.md)
  Returns an array of the current persistent domain names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/setpersistentdomain(_:forname:))*