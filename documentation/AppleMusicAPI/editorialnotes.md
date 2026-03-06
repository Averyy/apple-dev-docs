# EditorialNotes

**Framework**: Apple Music API  
**Kind**: dictionary

An object that represents a notes attribute.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object EditorialNotes
```

#### Discussion

Notes may include XML tags for formatting (`<b>` for bold, `<i>` for italic, or `<br>` for line break) and special characters (`&amp;` for `&`, `&lt;` for `<`, `&gt;` for `>`, `&apos;` for `‘`, and `&quot;` for `“`).

## Properties

- `short` (string): Abbreviated notes shown inline or when the content appears alongside other content.
- `standard` (string): Notes shown when the content is prominently displayed.
- `name` (string): Name for the editorial notes.
- `tagline` (string): The tag line for the editorial notes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/editorialnotes)*