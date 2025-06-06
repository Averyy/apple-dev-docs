# applinks.Details.Components.Query

**Framework**: Bundle Resources  
**Kind**: dictionary

A dictionary of names and values to match with query items in a URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
object applinks.Details.Components.Query
```

#### Discussion

The keys in this dictionary are [`NSURLQueryItem`](https://developer.apple.com/documentation/Foundation/NSURLQueryItem) names and the values are patterns to match with the specified key’s value. This example code shows how to use a dictionary object for pattern matching with a URL query component:

```javascript
"?": { "productID": "12345" }
```

The above definition matches a URL query component that has a name of `productID` and a value of `12345`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/applinks/details-swift.dictionary/components-swift.dictionary/query)*