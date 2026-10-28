# queryWithNode:forRecordTypes:attribute:matchType:queryValues:returnAttributes:maximumResults:error:

**Framework**: Open Directory  
**Kind**: method  
**Role**: Type Method

Returns an autoreleased query object created with provided parameters.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```objc
+ (ODQuery *) queryWithNode:(ODNode *) inNode forRecordTypes:(id) inRecordTypeOrList attribute:(ODAttributeType) inAttribute matchType:(ODMatchType) inMatchType queryValues:(id) inQueryValueOrList returnAttributes:(id) inReturnAttributeOrList maximumResults:(NSInteger) inMaximumResults error:(NSError **) outError;
```

## Return Value

The initialized query.

## Parameters

- `inNode`: The node to query.
- `inRecordTypeOrList`: The type or types of record to query. Can be an `NSString` object for a single type or an `NSArray` object containing `NSString` objects for multiple types.
- `inAttribute`: The name of the attribute to query.
- `inMatchType`: The type of query.
- `inQueryValueOrList`: The value or values to query in the attribute. Can be an `NSString` object or an `NSData` object for a single value, or an `NSArray` containing `NSString` and `NSData` objects for multiple values.
- `inReturnAttributeOrList`: The attribute or attributes to be returned from the query. Can be an `NSString` object for a single attribute or an `NSArray` object containing `NSString` objects for multiple attributes. Passing `nil` is equivalent to passing `kODAttributeTypeStandardOnly`.
- `inMaximumResults`: The maximum number of values to be returned.
- `outError`: An error reference for error details. Can be `nil`.

## See Also

### Creating and Initializing a Query
- [init(node: ODNode!, forRecordTypes: Any!, attribute: String!, matchType: ODMatchType, queryValues: Any!, returnAttributes: Any!, maximumResults: Int) throws](./init%28node,forrecordtypes,attribute,matchtype,queryvalues,returnattributes,maximumresults%29.md)
  Creates a query object with provided parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquery/querywithnode:forrecordtypes:attribute:matchtype:queryvalues:returnattributes:maximumresults:error:)*