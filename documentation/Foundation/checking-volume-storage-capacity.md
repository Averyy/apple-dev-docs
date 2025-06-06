# Checking Volume Storage Capacity

**Framework**: Foundation

Confirm that you have enough local storage space for a large amount of data.

#### Overview

Before you try to store a large amount of data locally, first verify that you have sufficient storage capacity. To get the storage capacity of a volume, you construct a URL (using an instance of [`URL`](url.md))  that references an object on the volume to be queried, and then query that volume.

##### Decide Which Query Type to Use

The query type to use depends on what’s being stored. If you’re storing data based on a user request or resources the app requires to function properly (for example, a video the user is about to watch or resources that are needed for the next level in a game), query against [`volumeAvailableCapacityForImportantUsageKey`](urlresourcekey/volumeavailablecapacityforimportantusagekey.md). However, if you’re downloading data in a more predictive manner (for example, downloading a newly available episode of a TV series that the user has been watching recently), query against [`volumeAvailableCapacityForOpportunisticUsageKey`](urlresourcekey/volumeavailablecapacityforopportunisticusagekey.md).

##### Construct a Query

Use this example as a guide to construct your own query:

## See Also

- [static let volumeAvailableCapacityKey: URLResourceKey](urlresourcekey/volumeavailablecapacitykey.md)
  Key for the volume’s available capacity in bytes (read-only).
- [static let volumeAvailableCapacityForImportantUsageKey: URLResourceKey](urlresourcekey/volumeavailablecapacityforimportantusagekey.md)
  Key for the volume’s available capacity in bytes for storing important resources (read-only).
- [static let volumeAvailableCapacityForOpportunisticUsageKey: URLResourceKey](urlresourcekey/volumeavailablecapacityforopportunisticusagekey.md)
  Key for the volume’s available capacity in bytes for storing nonessential resources (read-only).
- [static let volumeTotalCapacityKey: URLResourceKey](urlresourcekey/volumetotalcapacitykey.md)
  Key for the volume’s total capacity in bytes (read-only).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/checking-volume-storage-capacity)*