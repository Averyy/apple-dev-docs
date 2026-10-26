# tagHypothesesAtIndex:unit:scheme:maximumCount:tokenRange:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Finds multiple possible tags for a given linguistic unit, for a single scheme, at the specified character position.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```objc
- (NSDictionary<NSString *,NSNumber *> *) tagHypothesesAtIndex:(NSUInteger) characterIndex unit:(NLTokenUnit) unit scheme:(NLTagScheme) scheme maximumCount:(NSUInteger) maximumCount tokenRange:(NSRangePointer) tokenRange;
```

## Mentions

- [Identifying people, places, and organizations](../identifying-people-places-and-organizations.md)

#### Return Value

A tuple containing a dictionary and a range.

#### Discussion

Each dictionary entry is a predicted tag with its associated probability score. These tags are the top candidates proposed as possible tags for the token. The dictionary contains up to `maximumCount` entries.

The range contains the range of the individual token for which these tags were produced.

## Parameters

- `characterIndex`: The character index to begin examination.
- `unit`: The linguistic unit. See [`NLTokenUnit`](../nltokenunit.md) for possible values.
- `scheme`: The tag scheme. See [`NLTagScheme`](../nltagscheme.md) for possible values. Not all tag schemes produce more than one prediction.
- `maximumCount`: The maximum number of tag predictions to return.
- `tokenRange`: The range of the token for which the tags were produced.

## See Also

### Getting linguistic tags
- [- tagsInRange:unit:scheme:options:tokenRanges:](./tagsinrange_unit_scheme_options_tokenranges_.md)
  Finds an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [- tagAtIndex:unit:scheme:tokenRange:](./tagatindex_unit_scheme_tokenrange_.md)
  Finds a tag for a given linguistic unit, for a single scheme, at the specified character position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/taghypothesesatindex:unit:scheme:maximumcount:tokenrange:)*