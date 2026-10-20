# Ratings.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The attributes for a rating resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Ratings.Attributes
```

## Properties

- `value` (integer): The value for the resource’s rating. The possible values for the value key are `1` and `-1`. If a value isn’t present, the content doesn’t have a rating.

  **Allowed Values**: `-1`, `1`

## See Also

### Related Objects
- [object Ratings.Relationships](./relationships-data.dictionary.md)
  The relationships for a rating resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/ratings/attributes-data.dictionary)*