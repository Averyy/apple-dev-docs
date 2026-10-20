# CiXcodeVersion.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The attributes that describe an Xcode Versions resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiXcodeVersion.Attributes
```

## Topics

### Objects
- [object CiXcodeVersion.Attributes.TestDestinations](./attributes-data.dictionary/testdestinations-data.dictionary.md)
  The test destinations available for an Xcode version.

## Properties

- `name` (string): The name of the Xcode version.
- `testDestinations` ([CiXcodeVersion.Attributes.TestDestinations]): A list of the Xcode version’s available test destinations.
- `version` (string): The Xcode version.

## See Also

### Objects
- [object CiXcodeVersion.Relationships](./relationships-data.dictionary.md)
  The relationships of the Xcode Versions resource you included in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cixcodeversion/attributes-data.dictionary)*