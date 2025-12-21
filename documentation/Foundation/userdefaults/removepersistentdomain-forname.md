# removePersistentDomain(forName:)

**Framework**: Foundation  
**Kind**: method

Removes the keys and values from the specified persistent domain.

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

This method removes all of the keys and values from the specified domain. After clearing the domain’s contents, this method generates a [`didChangeNotification`](userdefaults/didchangenotification.md) for registered observers.

## Parameters

- `domainName`: The name of the domain to clear. If you specify the identifier   for the argument or registration domain, this method throws an exception.

## See Also

- [func persistentDomain(forName: String) -> [String : Any]?](userdefaults/persistentdomain(forname:).md)
  Retrieves the settings from the specified persistent domain.
- [func setPersistentDomain([String : Any], forName: String)](userdefaults/setpersistentdomain(_:forname:).md)
  Replaces the keys and values in the specified domain with the new keys and values you supply.
- [func volatileDomain(forName: String) -> [String : Any]](userdefaults/volatiledomain(forname:).md)
  Retrieves the settings from the specified volatile domain.
- [func setVolatileDomain([String : Any], forName: String)](userdefaults/setvolatiledomain(_:forname:).md)
  Replaces the keys and values in the specified domain with the new keys and values you supply.
- [func removeVolatileDomain(forName: String)](userdefaults/removevolatiledomain(forname:).md)
  Removes the keys and values from the specified volatile domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/removepersistentdomain(forname:))*