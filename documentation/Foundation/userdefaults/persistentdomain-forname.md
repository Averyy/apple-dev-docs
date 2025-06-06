# persistentDomain(forName:)

**Framework**: Foundation  
**Kind**: method

Returns a dictionary representation of the defaults for the specified domain.

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

#### Return Value

A dictionary containing keys for each default name and their corresponding default values.

#### Discussion

Calling this method is equivalent to initializing a user defaults object with [`init(suiteName:)`](userdefaults/init(suitename:).md) passing `domainName` and calling the [`dictionaryRepresentation()`](userdefaults/dictionaryrepresentation().md) method on it.

## Parameters

- `domainName`: The name of the domain to be represented.

## See Also

- [func setPersistentDomain([String : Any], forName: String)](userdefaults/setpersistentdomain(_:forname:).md)
  Sets a dictionary for the specified persistent domain.
- [func removePersistentDomain(forName: String)](userdefaults/removepersistentdomain(forname:).md)
  Removes the contents of the specified persistent domain from the user’s defaults.
- [func persistentDomainNames() -> [Any]](userdefaults/persistentdomainnames.md)
  Returns an array of the current persistent domain names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/persistentdomain(forname:))*