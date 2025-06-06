# ODQueryCallback

**Framework**: Open Directory  
**Kind**: typealias

A callback function called as results from a scheduled query are returned.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias ODQueryCallback = (ODQueryRef?, CFArray?, CFError?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

Results from this function must be retained or copied. The results from any given call are partial. If both `inResults` and `inError` are `NULL`, the query has completed.

## See Also

- [typealias ODAttributeType](odattributetype.md)
  An Open Directory attribute type.
- [typealias ODAuthenticationType](odauthenticationtype.md)
  An Open Directory authentication type.
- [class ODContext](odcontext.md)
  An Open Directory context type.
- [class ODNodeRef](odnoderef.md)
  An Open Directory node type.
- [class ODQueryRef](odqueryref.md)
  An Open Directory query type.
- [class ODRecordRef](odrecordref.md)
  An Open Directory record type.
- [class ODSessionRef](odsessionref.md)
  An Open Directory session type.
- [typealias ODMatchType](odmatchtype.md)
  An Open Directory match type.
- [typealias ODNodeType](odnodetype.md)
  An Open Directory node type.
- [typealias ODRecordType](odrecordtype.md)
  An Open Directory record type.
- [_ODAttributeType](odattributetype.md)
  An Open Directory attribute type.
- [_ODAuthenticationType](odauthenticationtype.md)
  An Open Directory authentication type.
- [_ODRecordType](odrecordtype.md)
  An Open Directory record type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquerycallback)*