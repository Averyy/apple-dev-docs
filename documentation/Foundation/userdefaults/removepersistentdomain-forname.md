# removePersistentDomain(forName:)

**Framework**: Foundation  
**Kind**: method

Removes the contents of the specified persistent domain from the user’s defaults.

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
func removePersistentDomain(forName domainName: String)
```

#### Discussion

Calling this method is equivalent to initializing a user defaults object with [`init(suiteName:)`](userdefaults/init(suitename:).md) passing `domainName`, and calling the [`removeObject(forKey:)`](userdefaults/removeobject(forkey:).md) method on each of its keys.

When a persistent domain is changed, an [`didChangeNotification`](userdefaults/didchangenotification.md) is posted.

## Parameters

- `domainName`: The name of the domain to have its contents removed.

## See Also

- [func persistentDomain(forName: String) -> [String : Any]?](userdefaults/persistentdomain(forname:).md)
  Returns a dictionary representation of the defaults for the specified domain.
- [func setPersistentDomain([String : Any], forName: String)](userdefaults/setpersistentdomain(_:forname:).md)
  Sets a dictionary for the specified persistent domain.
- [func persistentDomainNames() -> [Any]](userdefaults/persistentdomainnames.md)
  Returns an array of the current persistent domain names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/removepersistentdomain(forname:))*