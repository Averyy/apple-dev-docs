# Creating auto-renewable subscription groups

**Framework**: App Store Connect API

Configure subscription groups with the App Store Connect API.

#### Overview

The App Store Connect API lets you create and configure auto-renewable subscriptions for your app. After you create an auto-renewable subscription, you can add metadata, such as a display name, description, and duration. You can also choose your subscription pricing, create promotional and introductory offers, and set up subscription offer codes. When your app is fully configured, you can submit your subscription for review. After you receive approval, you can make pricing changes and edit some metadata for your subscription.

##### Review App Store Connect Api Usage

To manage auto-renewable subscriptions with the App Store Connect API, you need to understand key concepts for using the API. If you’re new to using the App Store Connect API, make sure to read the documentation in the Essentials section of [`App Store Connect API`](AppStoreConnectAPI.md) and learn how to create API keys, generate JWTs, identify rate limits, and more.

To create and manage auto-renewable subscriptions, be sure you have one of the following user roles:

- `ACCOUNT_HOLDER`
- `ADMIN`
- `APP_MANAGER`

For the full list of App Store Connect user roles, see [`UserRole`](userrole.md) and [`Program Roles`](https://developer.apple.comhttps://developer.apple.com/support/roles).

##### Plan Your Subscription Offerings

Before you get started with creating your subscription, first identify which app to include this subscription in. To get the Apple ID of the app, use `GET /v1/apps` ([`List Apps`](get-v1-apps.md)) and search the resulting pages for the name of the app you want to use. In the response, make note of the `id` of that app, which appears in the following format:

```other
{
"data" : [ {
"type" : "apps",
"id" : "525463029",
....
```

> 💡 **Tip**:  You can also get the Apple ID of the app in App Store Connect.

To arrange your subscription groups, make sure to map out all your offerings clearly. The following table shows an example for planning your subscriptions in a subscription group. The example uses subscriptions for a series of ukulele lessons with different levels of instructor feedback and detail, available for various time periods.

| Subscription Name | Duration | Level of Detail (1 is greatest) | Price (in USD) |
| --- | --- | --- | --- |
| All Access | 1 Month | 1 | 24.99 |
| All Access | 1 Year | 1 | 149.99 |
| Ukulele Beginner Lessons | 1 Month | 3 | 9.99 |
| Ukulele Beginner Lessons | 1 Year | 3 | 49.99 |
| Ukulele Advanced Lessons | 1 Month | 2 | 19.99 |
| Ukulele Advanced Lessons | 1 Year | 2 | 99.99 |

##### Create Your Subscription Group

After you plan your subscription offerings, create a subscription group, which is the container for your subscriptions. You can create your subscription group by using `POST /v1/subscriptionGroups` ([`Create a Subscription Group`](post-v1-subscriptiongroups.md)) with a payload.

Here’s an example payload:

```other
{
  "data": {
    "type": "subscriptionGroups",
    "attributes": {
      "referenceName": "Ukulele Lessons"
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "6446148572"
        }
      }
    }
  }
}
```

> **Note**:  The `referenceName` field is internal and isn’t displayed to users. Use a descriptive string that’s useful for your own organization and recognition purposes.

Here’s an example response, truncated for clarity:

```other
{
  "data" : {
    "type" : "subscriptionGroups",
    "id" : "2000036297",
    "attributes" : {
      "referenceName" : "Ukulele Lessons"
    },
```

The response contains an `id` field in the primary `data` object. You need this ID for subsequent steps.

##### Create Your Subscription Group Localization

Your localized subscription group name shows up in your app when a user goes through the process of reviewing or purchasing your auto-renewable subscription. To add a localization to your subscription group, you need the `id` of the subscription group from the previous step.

Use `POST /v1/subscriptionGroupLocalizations` ([`Create a Subscription Group Localization`](post-v1-subscriptiongrouplocalizations.md)) with a payload that specifies the localized name of the subscription group, the locale that you’re adding, and an optional custom app name. Depending on your app and subscriptions, you might need to add many localizations. If that’s the case, you can add many in one call to `/v1/subscriptionGroupLocalizations`.

Here’s an example payload:

```other
{
  "data": {
    "type": "subscriptionGroupLocalizations",
    "attributes": {
      "name": "Ukulele Lessons",
      "locale": "en-AU",
      "customAppName": "The Best Ukulele Lessons"
    },
    "relationships": {
      "subscriptionGroup": {
        "data": {
          "type": "subscriptionGroups",
          "id": "2000036297"
        }
      }
    }
  }
}
```

After you configure your subscription group, create your subscription following the steps in [`Managing auto-renewable subscriptions`](managing-auto-renewable-subscriptions.md).

## See Also

- [Subscription Groups](subscription-groups.md)
  Create, modify, and delete subscription groups for your app.
- [Subscription Group Localizations](subscription-group-localizations.md)
  Create, modify, and delete localized metadata for subscription groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/creating-auto-renewable-subscription-groups)*