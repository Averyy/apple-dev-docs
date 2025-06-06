# applinks

**Framework**: Bundle Resources  
**Kind**: dictionary

The root object for a universal links service definition.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
object applinks
```

#### Overview

Use this object to define the universal links you want to associate with your domain.

The object contains these keys:

Add the JSON code to your `apple-app-site-association` file along with the app identifiers for the apps that you designate to handle universal links for your domain. This example code shows a universal links section in an association file:

```javascript
"applinks": {
  "details": [
    {
      "appIDs": [ "ABCDE12345.com.example.app", "ABCDE12345.com.example.app2" ],
      "components": [
        {
          "#": "no_universal_links",
          "exclude": true,
          "comment": "Matches any URL whose fragment equals no_universal_links and instructs the system not to open it as a universal link"
        },
        {
          "/": "/buy/*",
          "comment": "Matches any URL whose path starts with /buy/"
        },
        {
          "/": "/help/website/*",
          "exclude": true,
          "comment": "Matches any URL whose path starts with /help/website/ and instructs the system not to open it as a universal link"
        },
        {
          "/": "/help/*",
          "?": { "articleNumber": "????" },
          "comment": "Matches any URL whose path starts with /help/ and that has a query item with name 'articleNumber' and a value of exactly 4 characters"
        }
      ]
    }
  ]
}
```

## Topics

### Universal links definitions
- [object applinks.Details](applinks/details-swift.dictionary.md)
  A list of apps and the universal links they handle for a domain.
### Pattern-matching defaults
- [object applinks.Defaults](applinks/defaults-swift.dictionary.md)
  An object that defines the default settings to use for universal links pattern matching.
### Substitution variables
- [object applinks.SubstitutionVariables](applinks/substitutionvariables-swift.dictionary.md)
  A list of named strings and an associated array of string values that define custom substitution variables to use for URL pattern matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/applinks)*