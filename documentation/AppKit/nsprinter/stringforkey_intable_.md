# stringForKey:inTable:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the first occurrence of a value associated with specified key.

**Availability**:
- macOS 10.0+ - Deprecated in 10.9

## Declaration

```objc
- (NSString *) stringForKey:(NSString *) key inTable:(NSString *) table;
```

#### Return Value

The value for the specified key, or `nil` if the key is not in the table. The returned string may also be empty.

#### Discussion

If `key` is a main keyword only, and if that keyword has options in the PPD file, this method returns an empty string. Use [`stringListForKey:inTable:`](./stringlistforkey_intable_.md) to retrieve the values for all occurrences of a main keyword.

## Parameters

- `key`: The key whose value you want.
- `table`: The name of a table from the printer’s PPD file.

## See Also

### Deprecated methods
- [- isKey:inTable:](./iskey_intable_.md)
  Returns a Boolean value that indicates whether the specified key is in the specified table.
- [- stringListForKey:inTable:](./stringlistforkey_intable_.md)
  Returns an array of strings, one for each occurrence, associated with specified key.
- [- booleanForKey:inTable:](./booleanforkey_intable_.md)
  Returns the Boolean value associated with the specified key.
- [- floatForKey:inTable:](./floatforkey_intable_.md)
  Returns the floating-point value associated with the specified key.
- [- intForKey:inTable:](./intforkey_intable_.md)
  Returns the integer value associated with the specified key.
- [- rectForKey:inTable:](./rectforkey_intable_.md)
  Returns the rectangle associated with the specified key.
- [- sizeForKey:inTable:](./sizeforkey_intable_.md)
  Returns the size data type associated with the specified key.
- [- statusForTable:](./statusfortable_.md)
  Returns the status of the specified table.
- [+ printerWithName:domain:includeUnavailable:](./printerwithname_domain_includeunavailable_.md)
  Deprecated.
- [- acceptsBinary](./acceptsbinary.md)
  Deprecated.
- [- domain](./domain.md)
  Deprecated.
- [- host](./host.md)
  Deprecated.
- [- imageRectForPaper:](./imagerectforpaper_.md)
  Deprecated.
- [- isColor](./iscolor.md)
  Deprecated.
- [- isFontAvailable:](./isfontavailable_.md)
  Deprecated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/stringforkey:intable:)*