# StatusTestBooleanValue

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

A test status item for a Boolean value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```
object StatusTestBooleanValue
```

#### Discussion

##### Status item availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in user scope | macOS, Shared iPad |

##### Status item example

```json
{
    "test": {
        "boolean-value": true
    }
}
```

## Properties

- `test.boolean-value` (boolean) *(required)*: The test status Boolean value.

## See Also

### Test items
- [object StatusTestArrayValue](./statustestarrayvalue.md)
  A test status item for an array.
- [object StatusTestDictionaryValue](./statustestdictionaryvalue.md)
  A test status item for a dictionary.
- [object StatusTestErrorValue](./statustesterrorvalue.md)
  A test status item for an error.
- [object StatusTestIntegerValue](./statustestintegervalue.md)
  A test status item for an integer.
- [object StatusTestRealValue](./statustestrealvalue.md)
  A test status item for a real value.
- [object StatusTestStringValue](./statusteststringvalue.md)
  A test status item for a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statustestbooleanvalue)*