# persistentDomain(forName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Retrieves the settings from the specified persistent domain.

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
func persistentDomain(forName domainName: String) -> [String : Any]?
```

```objc
- (NSDictionary<NSString *,id> *) persistentDomainForName:(NSString *) domainName;
```

## Return Value

A dictionary containing the keys and values from the specified domain. If the domain doesn’t contain any keys, or is a volatile domain, the method returns `nil`.

## Discussion

This method retrieves only the keys and values from the specified domain. It doesn’t retrieve keys from other persistent or volatile domains.

## Parameters

- `domainName`: The name of the persistent domain. Specify your app’s bundle identifier to retrieve any app-specific keys. Specify the [`globalDomain`](./globaldomain.md) identifier to retrieve keys in the global domain.

## See Also

### Managing domain-specific values
- [func setPersistentDomain([String : Any], forName: String)](./setpersistentdomain%28_,forname%29.md)
  Replaces the keys and values in the specified domain with the new keys and values you supply.
- [func volatileDomain(forName: String) -> [String : Any]](./volatiledomain%28forname%29.md)
  Retrieves the settings from the specified volatile domain.
- [func setVolatileDomain([String : Any], forName: String)](./setvolatiledomain%28_,forname%29.md)
  Replaces the keys and values in the specified domain with the new keys and values you supply.
- [func removePersistentDomain(forName: String)](./removepersistentdomain%28forname%29.md)
  Removes the keys and values from the specified persistent domain.
- [func removeVolatileDomain(forName: String)](./removevolatiledomain%28forname%29.md)
  Removes the keys and values from the specified volatile domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/persistentdomain(forname:))*