# DateComponents

**Framework**: SiriKit Cloud Media  
**Kind**: typealias  
**Role**: Type

A full or partial date and time.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
* DateComponents
```



**Allowed Types**: `string(/[0-9]{4}/)`, `string(/[0-9]{4}-[0-9]{2}/)`, `date`, `date-time`, `ExplicitDateComponents`

## Discussion

The client may provide an [`ExplicitDateComponents`](./explicitdatecomponents.md) object or represent a Gregorian date in one of the following formats:

| Description | Format | Example |
| --- | --- | --- |
| Year only | `string` (pattern: `/[0-9]{4}/)` | `1984` |
| Year and month | `string`  (pattern:`/[0-9]{4}-[0-9]{2}/)` | `1984-01` |
| Full date without time | `date` | `1984-01-22` |
| Date and time | `date-time` | `1984-01-22T01:23:45.678Z` |

## See Also

### Filtering by Release Date
- [object DateComponentsRange](./datecomponentsrange.md)
  A period of time from a specified start date to a specified end date.
- [object ExplicitDateComponents](./explicitdatecomponents.md)
  A date or time in specified of units (such as year, month, day, hour, and minute) for evaluation in a calendar system and time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/datecomponents)*