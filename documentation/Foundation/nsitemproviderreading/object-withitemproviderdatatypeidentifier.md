# object(withItemProviderData:typeIdentifier:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Creates a new instance of a class using the given data and UTI string.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static func object(withItemProviderData data: Data, typeIdentifier: String) throws -> Self
```

#### Return Value

An object created from the given data.

## Parameters

- `data`: The data used to create the object.
- `typeIdentifier`: The uniform type identifier (UTI) representing the data type of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemproviderreading/object(withitemproviderdata:typeidentifier:))*