# setVolatileDomain(_:forName:)

**Framework**: Foundation  
**Kind**: method

Replaces the keys and values in the specified domain with the new keys and values you supply.

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
func setVolatileDomain(_ domain: [String : Any], forName domainName: String)
```

#### Discussion

This method removes the existing keys from the specified domain and then adds the new keys you provide. After updating the keys, this method generates a [`didChangeNotification`](userdefaults/didchangenotification.md) for registered observers.

## Parameters

- `domain`: A dictionary of keys and values to assign to the domain.
- `domainName`: The name of the domain to update.

## See Also

- [func persistentDomain(forName: String) -> [String : Any]?](userdefaults/persistentdomain(forname:).md)
  Retrieves the settings from the specified persistent domain.
- [func setPersistentDomain([String : Any], forName: String)](userdefaults/setpersistentdomain(_:forname:).md)
  Replaces the keys and values in the specified domain with the new keys and values you supply.
- [func volatileDomain(forName: String) -> [String : Any]](userdefaults/volatiledomain(forname:).md)
  Retrieves the settings from the specified volatile domain.
- [func removePersistentDomain(forName: String)](userdefaults/removepersistentdomain(forname:).md)
  Removes the keys and values from the specified persistent domain.
- [func removeVolatileDomain(forName: String)](userdefaults/removevolatiledomain(forname:).md)
  Removes the keys and values from the specified volatile domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/setvolatiledomain(_:forname:))*