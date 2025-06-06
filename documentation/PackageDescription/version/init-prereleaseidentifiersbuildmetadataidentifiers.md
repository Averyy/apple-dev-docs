# init(_:_:_:prereleaseIdentifiers:buildMetadataIdentifiers:)

**Framework**: Packagedescription  
**Kind**: init

Initializes a version struct with the provided components of a semantic version.

## Declaration

```swift
init(_ major: Int, _ minor: Int, _ patch: Int, prereleaseIdentifiers: [String] = [], buildMetadataIdentifiers: [String] = [])
```

#### Discussion

> **Note**: `major >= 0 && minor >= 0 && patch >= 0`.

> **Note**: `prereleaseIdentifiers` can contain only ASCII alpha-numeric characters and “-”.

> **Note**: `buildMetaDataIdentifiers` can contain only ASCII alpha-numeric characters and “-”.

## Parameters

- `major`: The major version number.
- `minor`: The minor version number.
- `patch`: The patch version number.
- `prereleaseIdentifiers`: The pre-release identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/version/init(_:_:_:prereleaseidentifiers:buildmetadataidentifiers:))*