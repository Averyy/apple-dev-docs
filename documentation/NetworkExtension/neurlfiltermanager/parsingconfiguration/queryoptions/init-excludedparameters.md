# init(excluded:parameters:)

**Framework**: Network Extension  
**Kind**: init

Creates a new query options configuration with default values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
init(excluded: Bool = false, parameters: [String]? = nil)
```

#### Discussion

The query options default behavior is as follows:

- Parsing includes the query.
- Parsing includes all parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/queryoptions/init(excluded:parameters:))*