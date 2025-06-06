# applinks.Details

**Framework**: Bundle Resources  
**Kind**: dictionary

A list of apps and the universal links they handle for a domain.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
object applinks.Details
```

#### Discussion

The object optionally contains any of these keys:

Use `appID` or `appIDs` to specify the applications that can access the specific URLs you define in the associated `components` array. You specify each application identifier in the following format:

```javascript
<Application Identifier Prefix>.<Bundle Identifier>
```

This example code shows a universal links details object in an association file:

```javascript
{
  "appIDs": [ "ABCDE12345.com.example.app", "ABCDE12345.com.example.app2" ],
  "components": [
    {
      "/": "/buy/*",
      "#": "my_great_product_123",
      "comment": "Matches any URL whose path starts with /buy/ and fragment equals my_great_product_123, ignoring case"
    }
  ],
  "defaults": { "caseSensitive": false }
}
```

## Topics

### URL components
- [object applinks.Details.Components](applinks/details-swift.dictionary/components-swift.dictionary.md)
  Patterns that define the universal links an app can open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/applinks/details-swift.dictionary)*