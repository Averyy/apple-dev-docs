# queryItemWithName:value:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a new query item with the specified name and value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) queryItemWithName:(NSString *) name value:(NSString *) value;
```

#### Return Value

A new query item object.

#### Discussion

To use the newly initialized query item in composing a URL, add it to the [`queryItems`](../nsurlcomponents/queryitems.md) array of an [`NSURLComponents`](../nsurlcomponents.md) instance. Because assigning an array of query items to an [`NSURLComponents`](../nsurlcomponents.md) instance automatically encodes the name and value properties, you should not percent-encode these strings.

## Parameters

- `name`: The name of the query item. For example, in the URL `http://www.apple.com/search/?q=iPad`, the `name` parameter is `q`.
- `value`: The value for the query item. For example, in the URL `http://www.apple.com/search/?q=iPad`, the `value` parameter is `iPad`.

## See Also

### Creating a Query Item
- [init(name: String, value: String?)](./init%28name,value%29.md)
  Initializes a newly allocated query item with the specified name and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlqueryitem/queryitemwithname:value:)*