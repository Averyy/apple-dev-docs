# Get the user's replay data

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the user’s replay data for the latest eligible year.

**Availability**:
- Apple Music 1.0+

#### Discussion

A successful HTTP request returns music summaries for the most recent year that the user has enough listening history. If unsuccessful, the HTTP status code indicates the error, and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-the-user's-replay-data)*