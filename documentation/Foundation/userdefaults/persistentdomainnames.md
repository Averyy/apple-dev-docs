# persistentDomainNames()

**Framework**: Foundation  
**Kind**: method

Returns an array of the current persistent domain names.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func persistentDomainNames() -> [Any]
```

#### Return Value

An array of `NSString` objects containing the domain names.

#### Discussion

You can get the keys and values for each domain by passing the returned domain names to the  [`persistentDomain(forName:)`](userdefaults/persistentdomain(forname:).md) method.

## See Also

- [func persistentDomain(forName: String) -> [String : Any]?](userdefaults/persistentdomain(forname:).md)
  Returns a dictionary representation of the defaults for the specified domain.
- [func setPersistentDomain([String : Any], forName: String)](userdefaults/setpersistentdomain(_:forname:).md)
  Sets a dictionary for the specified persistent domain.
- [func removePersistentDomain(forName: String)](userdefaults/removepersistentdomain(forname:).md)
  Removes the contents of the specified persistent domain from the user’s defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/persistentdomainnames())*