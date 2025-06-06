# Getting value based on age using an array

**Framework**: App Store Connect API

Return a value that changes according to an array of values as a function of the age of the requests.

#### Overview

Use the `agedValues()` function in the expression of a matchmaking rule to loosen matchmaking criteria over time. This function returns a value that changes based on the given arrays and depending on the age of requests. Use this function instead of `agedAsSteppedValue()` when you want more control over the values.

For example, pass the following parameters to this function:

```other
agedValues(age, `5`, [ `20`, `30`, `40`, `50`, `60`, `100` ], 
                     [  `5`, `10`, `15`, `20`, `25`, `30` ])
```

If the `ageSeconds` parameter is `3` (less than the first item in the `ages` array), the value is `5`. If `ageSeconds` is `17`, the value is `40`. If `ageSeconds` is `32` (greater than the last item in the `ages` array), the value is `100`.

| Age range | Return value |
| --- | --- |
| `[0, 4]` | `5` |
| `[5, 9]` | `20` |
| `[10, 14]` | `30` |
| `[15, 19]` | `40` |
| `[20, 24]` | `50` |
| `[25, 29]` | `60` |
| `[30, 30+]` | `100` |

To loosen constraints over time, use the results of this function in comparisons. For example, compare the sum of all the player counts to a value that decreases with the average age of candidate requests that the matchmaking algorithm selects.

```other
agedValues(avg(requests[].secondsInQueue), 8, [ 6, 4, 2], [ 10, 15, 20 ]) <= sum(requests[].playerCount)
```

##### Declaration

```other
number agedValues(number        $ageSeconds, 
                  number        $initialValue,
                  array[number] $values, 
                  array[number] $ages)
```

##### Parameters

| `ageSeconds` | The average, maximum, or minimum age of match requests in the queue. |
| --- | --- |
| `initialValue` | The value for `ages` that are less than the first item in the `ages` array |
| `values` | The values to map the age ranges to. |
| `ages` | The age ranges to map to the values. |

##### Return Value

If `ageSeconds` is less than the first item in the `ages` array (`ages[0]`), `initialValue`. If `ageSeconds` is in the range between two items in the `ages` array (`ages[n] <= ageSeconds < ages[n+1]`), the corresponding item in the `values` array (`values[n]`). If `ageSeconds` is greater than the last item in the `ages` array, `initialValue`.

## See Also

- [Getting value based on age](getting-value-based-on-age.md)
  Return a value that changes in regular steps as a function of the age of the requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/getting-value-based-on-age-using-an-array)*