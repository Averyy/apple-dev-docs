# Getting value based on age

**Framework**: App Store Connect API

Return a value that changes in regular steps as a function of the age of the requests.

#### Overview

Use the `agedAsSteppedValue()` function in the expression of a matchmaking rule to get a value that depends on the age of a request. You can use this function in combination with others to create a criteria that loosen over time.

For example, `agedAsSteppedValue(age, `50`, `500`, `10`, `50`)` — where `ageIntervalSeconds` is `10`, `intervalChange` is `50`, and `finalLimit` is `500` — maps the `ageSeconds` parameter to the values in the table below. If `age` is `3`, the function returns `50`, if `age` is `11`, it returns `150`, and if `age` is `84`, it returns `500`.

| Age range | Return value |
| --- | --- |
| `[0,9]` | `50` |
| `[10, 19]` | `150` |
| `[20, 29]` | `250` |
| `[30, 39]` | `350` |
| `[40, 49]` | `450` |
| `[50, 50+]` | `500` |

If you pass a negative value for the `intervalChange` and `finalLimit` parameters, the values decrement as the `age` increases. For example, `agedValueLinear(age, `8`, `-4`, `5`, `-2`)` maps the `ageSeconds` parameter to the values in the table below.

| Age range | Return value |
| --- | --- |
| `[0, 4]` | `8` |
| `[5, 9]` | `4` |
| `[10, 14]` | `2` |
| `[15, 19]` | `0` |
| `[20, 24]` | `-2` |
| `[25, 25+]` | `-4` |

To loosen constraints over time, use this function in comparisons. For example, use this function in an expression to constrain matches to players with similar skill levels. Start with the difference in skill set to `20`, and as the average age of the requests increases by `10` seconds, increase the difference by `20` until it reaches the maximum of `100`.

```other
diff(requests[].properties.skill) <= agedValues(avg(requests[].secondsInQueue), 20, 100, 10, 20)
```

To compute the average age of the requests in the queue, pass `requests[].secondsInQueue` to the `avg()` function. Alternatively, you can get the minimum or maximum age of the requests using the JMESPath `min()` and `max()` functions.

##### Declaration

```other
number agedAsSteppedValue(number $ageSeconds, number $initialValue, number $finalLimit, number ageIntervalSeconds, number $intervalChange)
```

##### Parameters

##### Return Value

A linear-stepped value that increments or decrements by the given amount based on the ageSeconds parameter. If ageSeconds is less than intervalChange, returns initialValue. Otherwise, returns the result of this equation that maps ageSeconds to a range of values:

```swift
$initialValue + $intervalChange * ( $ageSeconds / $ageIntervalSecs )
```

If the result is greater than `finalLimit`, returns `finalLimit` instead.

## See Also

- [Getting value based on age using an array](getting-value-based-on-age-using-an-array.md)
  Return a value that changes according to an array of values as a function of the age of the requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/getting-value-based-on-age)*