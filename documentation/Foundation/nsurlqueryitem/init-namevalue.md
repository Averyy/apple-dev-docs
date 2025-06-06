# init(name:value:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated query item with the specified name and value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(name: String, value: String?)
```

#### Return Value

An initialized query item object.

#### Discussion

To use the newly initialized query item in composing a URL, add it to the [`queryItems`](nsurlcomponents/queryitems.md) array of an [`NSURLComponents`](nsurlcomponents.md) instance. Because assigning an array of query items to an [`NSURLComponents`](nsurlcomponents.md) instance automatically encodes the name and value properties, you should not percent-encode these strings.

## Parameters

- `name`: The name of the query item. For example, in the URL  , the   parameter is  .
- `value`: The value for the query item. For example, in the URL  , the   parameter is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlqueryitem/init(name:value:))*