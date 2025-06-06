# applinks.Details.Components

**Framework**: Bundle Resources  
**Kind**: dictionary

Patterns that define the universal links an app can open.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
object applinks.Details.Components
```

#### Discussion

Use this object to define whether an associated app can open specific URLs in this domain as universal links.

The object optionally contains any of these keys:

The order that you use to specify the patterns in the array determines the order the system follows when looking for a match. The first match wins, allowing you to designate one app to handle specified URLs in your website, and another app to handle the rest.

You can also use the following wildcards in your URL pattern-matching definitions:

`*` — Matches zero or more characters. This performs a greedy match and matches as many characters as possible.

`?` — Matches any single character.

In addition, you can use `?*` to match one or more characters (that is, at least one character).

A match occurs when a URL matches  the components that a `components` object specifies. The following example code matches all URLs with a path of `abc` and a query of `def`.

```javascript
{
  "/": "abc",
  "?": "def",
  "#": "*"
}
```

The URL `https://www.example.com/abc?def` matches with the above code, but `https://www.example.com/abc` and `https://www.example.com?def` don’t. The fragment part of the code matches everything, so the system ignores it.

This example code shows another components object in an association file:

```javascript
{
  "/": "/help/website/*",
  "exclude": true,
  "comment": "Matches any URL whose path starts with /help/website/ and instructs the system not to open it as a universal link"
}
```

## Topics

### Query dictionaries
- [object applinks.Details.Components.Query](applinks/details-swift.dictionary/components-swift.dictionary/query.md)
  A dictionary of names and values to match with query items in a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/applinks/details-swift.dictionary/components-swift.dictionary)*