# Checking Your Reservation Markup

**Framework**: Siri Event Suggestions Markup

Preview your reservation event data before the Allow List includes your domain.

#### Overview

Siri only handles event suggestions in emails and webpages from domains on a Siri Events Allow List. To apply for the Allow List, you need working examples of your reservation webpages and emails. Full application details are available on the [`Siri Event Suggestions Allow List Form`](https://developer.apple.comhttps://developer.apple.com/contact/request/siri-events/).

While building your markup and preparing your examples, you may bypass the Allow List on a test device to check that the system can parse your events correctly.

##### Test Without Authentication on Ios or Ipados

You can bypass Siri’s authentication measures on a development device or in the simulator to test your data format:

- Open the Settings app, navigate to Developer, and find the Siri Event Suggestions Testing section.
- Enable Allow Any Domain to process emails and webpages before your organization’s domain is on the Allow List.
- Enable Allow Unverified Sources for Mail and Safari to bypass DKIM or SSL authenticity verification on emails and webpages.

##### Test Without Authentication on Macos

You can also bypass Siri’s authentication measures to test your data format with Mail or Safari on a Mac.

To process emails and webpages from a domain which hasn’t been added to the Allow List, enter the following command in Terminal:

```bash
defaults write com.apple.suggestions SuggestionsAllowAnyDomainForMarkup -bool true
```

To bypass DKIM verification in Mail or SSL verification in Safari, enter this command in Terminal:

```bash
defaults write com.apple.suggestions SuggestionsAllowUnverifiedSourceForMarkup -bool true
```

##### Avoid Common Mistakes

Keep the [`reservationId`](reservationid.md) consistent whenever you refer to a particular reservation, so that Siri can apply any update or cancellation to the correct calendar event. Confirm that event information, such as duration and location, is displayed correctly in the Siri Event Suggestions calendar. Test with events that start in the future. Ensure that your data conveys schedules correctly even when your service, the user, the event start date, and the event end date are each in a different timezone.

## See Also

- [Providing Trusted Data](providing-trusted-data.md)
  Sign your content and avoid sending unnecessary or inaccurate information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/checking-your-reservation-markup)*