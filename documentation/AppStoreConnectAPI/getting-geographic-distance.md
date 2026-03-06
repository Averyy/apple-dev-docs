# Getting geographic distance

**Framework**: App Store Connect API

Return the relative geographic distance between two match requests.

#### Overview

Use the `geoLatency()` function in the expression of a matchmaking rule to get the geographic distance between two devices that submit match requests. This function uses the location of the players’ devices that the match request contains, but keeps that information private.

##### Declaration

```other
number geoLatency(object $request1, object $request2)
```

##### Parameters

- **`request1`**: A match request to compare with `request2`.
- **`request2`**: A match request to compare with `request1`.

##### Return Value

A value between `0.0` and `1.0` that represents the relative geographic distance between the player devices that issued these requests, where `0.0` is in the same local area and `1.0` is the longest possible distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/getting-geographic-distance)*